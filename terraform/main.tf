resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  user_data = file("user_data.sh")

  tags = {
    Name = "PythonMicroservices"
  }
}