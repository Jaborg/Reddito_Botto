provider "aws" {
  region = "eu-west-1"
}

resource "aws_launch_configuration" "example" {
  image_id      = "ami-02cad064a29d4550c"
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              echo "CLIENT_ID=${var.CLIENT_ID}" >> /etc/environment
              echo "CLIENT_SECRET=${var.CLIENT_SECRET}" >> /etc/environment
              echo "REDDIT_USERNAME=${var.REDDIT_USERNAME}" >> /etc/environment
              echo "PASSWORD=${var.PASSWORD}" >> /etc/environment
              echo "USER_AGENT=${var.USER_AGENT}" >> /etc/environment
              EOF

  provisioner "local-exec" {
    command = "docker-compose up -d"
  }
  # Required when using a launch configuration with an auto scaling group.
  lifecycle {
    create_before_destroy = true
  }
}

