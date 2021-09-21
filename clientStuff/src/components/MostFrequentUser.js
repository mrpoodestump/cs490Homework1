import React from "react";
import { useLazyQuery, gql } from "@apollo/client";
import { CircularProgress, Button } from "@mui/material";

const GET_ROW_COUNT = gql`
  {
    getMostFrequentUser {
      user_id
      user_name
      count
    }
  }
`;

const FrequentUser = () => {
  const [getMostFrequentUser, { data, loading, error }] = useLazyQuery(
    GET_ROW_COUNT
  );

  console.log(data);
  return (
    <>
      <Button onClick={() => getMostFrequentUser()}>Most Frequent User</Button>
      {data && (
        <div
          style={{
            backgroundColor: "#282c34",
            color: "white",
            padding: "10px",
            borderRadius: "5px",
          }}
        >
          {/* <ul>
            {data.getMostFrequentUser.map((item) => (
              <li>{item}</li>
            ))}
          </ul> */}
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

export default FrequentUser;
