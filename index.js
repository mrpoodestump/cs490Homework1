const { ApolloServer, PubSub } = require("apollo-server");
const typeDefs = require("./graphql/typeDefs");
const resolvers = require("./graphql/resolvers");
// const db = require("better-sqlite3")("tweet_example.db");

// const selectTableStatement = db.prepare("SELECT COUNT(*) FROM tweet_info");
// const entryCount = selectTableStatement.get();
// console.log(entryCount);

const port = 5000;

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server
  .listen({
    port: port,
  })
  .then((res) => {
    console.log(`Listening on port ${port}`);
  });
