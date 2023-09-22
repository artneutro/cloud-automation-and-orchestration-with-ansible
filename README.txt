Republic of Ireland
Department of Computer Science
Student: Jose Lo Huang

##################################
1. Introduction
##################################

This code is designed to create a grouop of EC2 instances and
install Apache2 on them.

##################################
2. Code
##################################

The files included on this package is as follows:

* Main-ansible.py = Manage the main program, create the playbooks and run the playbooks.
* CIT-DUB.pem = The secret key to connect to the Ansible master host.

Note: All the files must be on the same directory. 

2.1. How to Run 

The code was tested in Ubuntu Linux with Python 2.7. 

ssh -i CIT-DUB.pem ubuntu@X.X.X.X
./Main-ansible.py

2.2. Components dependencies tree

+- Main-ansible +- CIT-DUB.pem

2.3. Actions

* Request the number of webservers to create
* Create the playbook instance_launcher.yml
* Run the playbook instance_launcher.yml to create the servers
* Create the playbook instance_installer.yml
* Run the playbook instance_installer.yml to install Apache2 on the servers

##################################
3. Conclusion
##################################

After run this code, the user can create in an easy way a number of webservers
running Apache2 on Ubuntu Linux.

##################################
4. References 
##################################

These were the references used for the Ansible part of the project:

-- Playbook 1

https://www.ansible.com/
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu
https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_module.html
https://davelms.medium.com/use-ansible-to-create-and-configure-ec2-instances-on-aws-cfbb0ed019bf
https://www.mindbowser.com/how-to-create-ec2-instances-using-ansible/
https://aws.amazon.com/blogs/infrastructure-and-automation/automate-ansible-playbook-deployment-amazon-ec2-github/
https://www.reddit.com/r/ansible/comments/b417g8/how_do_you_authenticate_to_aws_ec2_instance_with/

-- Playbook 2
https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html
https://github.com/ansible/ansible/blob/stable-2.9/contrib/inventory/ec2.py
https://github.com/ansible/ansible/blob/stable-2.9/contrib/inventory/ec2.ini
https://medium.com/datadriveninvestor/devops-using-ansible-to-provision-aws-ec2-instances-3d70a1cb155f
https://dev.to/iamtito/ansible-dynamic-inventory-31n4
https://www.tecmint.com/use-static-and-dynamic-inventory-in-ansible/
https://medium.com/@iamrameshjonathan/create-aws-dynamic-inventory-using-ansible-8676e2f1e04
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html#apt-module
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04
https://my330space.wordpress.com/2019/12/06/install-apache2-on-ubuntu-with-ansible/
https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_module.html
https://docs.ansible.com/ansible/2.3/become.html
