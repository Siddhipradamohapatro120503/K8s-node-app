# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install 

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the app will run on
EXPOSE 5173

ENV HOST=0.0.0.0

# Define the command to run your app
CMD ["npm", "start"]
