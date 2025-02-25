resource "aws_instance" "my_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type

}

resource "aws_instance" "terraform_import_practice" {
  ami           = ""
  instance_type = "t2.nano"

}