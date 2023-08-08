$HOST= IP of managed node
sudo adduser ansible
sudo usermod -aG sudo ansible

#open sudoers file
sudo visudo
# ansible ALL=(ALL:ALL) NOPASSWD:ALL

# Move into Ansible directory for keygen process
cd Ansible

# Create new ssh keys for the ansible user at the controller
ssh-keygen -f ansible.key.pub $HOST

# Copy the public key to the managed node
ssh-copy-id -i ansible.key.pub $HOST

# Test
ansible -i hosts.yaml servers -m ping

