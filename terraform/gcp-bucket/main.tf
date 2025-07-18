provider "google" {
  credentials = file(var.chave_acesso)
  project     = var.project_id
  region      = var.region
}

resource "google_storage_bucket" "meu_bucket" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}

