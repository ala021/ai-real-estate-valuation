# 1. Use Node.js to run React
FROM node:18-alpine

# 2. Set working directory
WORKDIR /app

# 3. Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# 4. Copy the rest of the frontend code
COPY . .

# 5. Expose the standard React port
EXPOSE 3000

# 6. Start the app
CMD ["npm", "start"]