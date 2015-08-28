FROM ubuntu:14.04

# Install SSH
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:65RSJ1QU' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]


# Install FTP
RUN apt-get install -y vsftpd

ADD conf/vsftpd.conf /etc/
ADD conf/vsftpd.sh /root/

RUN mkdir -p /var/run/vsftpd/empty \
 && chmod +x /root/vsftpd.sh \
 && chown root:root /etc/vsftpd.conf

VOLUME /ftp/

EXPOSE 21/tcp

ENTRYPOINT ["/root/vsftpd.sh"]
CMD ["vsftpd"]
