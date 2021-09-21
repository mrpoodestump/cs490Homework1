import react, { useState } from "react";
import { CircularProgress, Button } from "@mui/material";
import { gql, useLazyQuery } from "@apollo/client";

//const { text, pythonError } = runFile;
const TEST_QUERY = gql`
  {
    runFile {
      text
      error
    }
  }
`;

function StreamData() {
  const [streamData, { data, loading, error }] = useLazyQuery(TEST_QUERY);

  return (
    <>
      <Button onClick={() => streamData()}> Stream</Button>

      {data && (
        <div
          style={{
            minWidth: "200px",
            minHeight: "200px",
            borderRadius: "10px",
            backgroundColor: "#282c34",
          }}
        >
          <div style={{ color: "white", padding: "10px" }}>
            {" "}
            We got data yo: {data.runFile.text}
          </div>
        </div>
      )}
      {loading && (
        <div>
          We're loading bitch...
          <CircularProgress></CircularProgress>
        </div>
      )}
      {error && <div>we're error bitch {error.message}</div>}
    </>
  );
}

export default StreamData;
