FROM node:20.12.2

WORKDIR /app
COPY . .

RUN npm install
RUN npm install -g @quasar/cli

EXPOSE 9000
CMD ["quasar", "dev"]
