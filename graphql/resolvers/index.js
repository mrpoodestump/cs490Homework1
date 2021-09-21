const runResolvers = require("./run");

module.exports = {
  Query: {
    ...runResolvers.Query,
  },
};
