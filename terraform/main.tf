provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = "your_ami_id"
  instance_type = "t2.micro"
  key_name      = "your_key_pair_name"

  user_data = <<-EOF
              #!/bin/bash
              docker pull your_docker_image
              docker run -d your_docker_image
              EOF
}

output "public_ip" {
  value = aws_instance.example.public_ip
}
