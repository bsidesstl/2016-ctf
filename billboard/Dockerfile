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
RUN apt-get install -y vsftpd libpam-pwdfile apache2-utils supervisor
RUN mkdir /etc/vsftpd \
 && mkdir -p /var/run/vsftpd/empty \
 && useradd --home /home --gid nogroup -m --shell /bin/false vsftpd

ADD conf/vsftpd.pam                        /etc/pam.d/vsftpd
ADD conf/vsftpd.conf                       /etc/vsftpd.conf
ADD conf/vsftpd_virtual_user.sh             /usr/bin/vsftpd_virtual_user
RUN chmod a+x /usr/bin/vsftpd_virtual_user

# Supervisor
RUN mkdir -p /var/log/supervisor
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Port
EXPOSE 20 21

# Daemon
CMD ["/usr/bin/supervisord"]
