const { gql } = require("apollo-server");

module.exports = gql`
  type Query {
    runFile: Info
    getRowCount: Int!
    getMostFrequentUser: MostFrequentUser
  }
  type Info {
    text: String
    error: String
  }
  type MostFrequentUser {
    user_id: Float
    user_name: String
    count: Float
  }
`;
