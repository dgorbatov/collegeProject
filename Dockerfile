FROM node:14.17

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV port=8080

EXPOSE 8080

CMD [ "npm", "start"]