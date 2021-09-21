const { spawn } = require("child_process");
const db = require("better-sqlite3")("tweet_example.db");

const pythonData = async () => {
  const child = spawn("python3", ["./index.py"]);

  let data = "";
  for await (const chunk of child.stdout) {
    console.log("stdout chunk: " + chunk);
    data += chunk;
  }
  let error = null;
  for await (const chunk of child.stderr) {
    console.error("stderr chunk: " + chunk);
    error += chunk;
  }
  const exitCode = await new Promise((resolve, reject) => {
    child.on("close", resolve);
  });

  if (exitCode) {
    throw new Error(`subprocess error exit ${exitCode}, ${error}`);
  }
};

module.exports = {
  Query: {
    runFile: async () => {
      pythonData();
      return {
        text: "attempting to run python streaming",
        error: null,
      };
    },
    getRowCount: async () => {
      const selectTableStatement = db.prepare(
        "SELECT COUNT(*) FROM tweet_info"
      );
      const entryCount = selectTableStatement.get();
      console.log(entryCount);
      return entryCount["COUNT(*)"];
    },
    getMostFrequentUser: async () => {
      const getMostFrequentUserStatement = db.prepare(
        "SELECT user_id, COUNT(user_id) AS user_id_count FROM tweet_info GROUP BY user_id ORDER BY user_id_count DESC"
      );
      const frequentUser = getMostFrequentUserStatement.all();
      console.log(frequentUser);
      const user_id = frequentUser["user_id"];
      const user_id_count = frequentUser["user_id_count"];

      const getMostFrequentUserName = db.prepare(
        "SELECT user_id, tweet_id, tweet_text, COUNT(retweet_count) AS retweet_count FROM tweet_info ORDER BY retweet_count DESC"
      );
      const userName = getMostFrequentUserName.get();
      console.log(userName);
      //const user_screen_name = userName["user_screen_name"];
      //console.log(returnObj);

      return {
        user_id: null,
        user_name: null,
        count: null,
      };
    },
  },
};
