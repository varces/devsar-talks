# [START all]
FROM node:10-alpine
EXPOSE 8080
COPY server.js .
CMD node server.js
# [END all]
