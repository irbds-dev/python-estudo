variable "pais" {
  type = string
  default = "Brasil"
  description = "Em qual país você está?"
}

variable "idade" {
  type = number
  description = "Qual é a sua idade?"
}

variable "nome" {
  type = string
  description = "Qual seu nome?"
}

variable "estuda" {
  type = bool
  default = true
  description = "Você esta estudando?"
}

output "pais" {
  value = var.pais
  description = "Seu país: "
}

output "idade" {
  value = var.pais
  description = "Sua idade: "
}

output "nome" {
  value = var.nome
  description = "Seu nome: "
}

output "estuda" {
  value = var.estuda
  description = "Está estudando: "
}
