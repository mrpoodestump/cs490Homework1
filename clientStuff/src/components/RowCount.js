import React from "react";
import { useLazyQuery, gql } from "@apollo/client";
import { CircularProgress, Button } from "@mui/material";

const GET_ROW_COUNT = gql`
  {
    getRowCount
  }
`;

const RowCount = () => {
  const [getRowCount, { data, loading, error }] = useLazyQuery(GET_ROW_COUNT);
  console.log(data);
  return (
    <>
      <Button onClick={() => getRowCount()}>RowCount</Button>
      {data && (
        <div
          style={{
            backgroundColor: "#282c34",
            color: "white",
            padding: "10px",
            borderRadius: "5px",
          }}
        >
          Number of Rows: {data.getRowCount}
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
};

export default RowCount;
