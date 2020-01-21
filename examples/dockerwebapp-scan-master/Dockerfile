# Download base image ubuntu 16.04
#FROM ubuntu:16.04
FROM python:3-onbuild

# COPY startup script into known file location in container
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Install dependencies
#RUN pip install -r requirements.txt
 
# Expose port
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!
