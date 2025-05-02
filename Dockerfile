# Use the official PostgreSQL image as a base
FROM postgres:latest

# Set environment variables for database creation
# Note: Use more secure passwords in production
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Copy the SQL script to initialize the database
# Scripts in /docker-entrypoint-initdb.d are run automatically
COPY create-data.sql /docker-entrypoint-initdb.d/
