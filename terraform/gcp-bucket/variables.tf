variable "project_id" {
  description = "ID do projeto no GCP"
  type        = string
}

variable "region" {
  description = "Região onde o bucket será criado"
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Nome do bucket"
  type        = string
}

variable "chave_acesso" {
  description = "Caminho da chave"
  type        = string
}
