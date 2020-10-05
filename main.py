import requests

print('Insira seu nome de usuário GitHub: ')
username = input()

response = requests.get(
  'https://api.github.com/users/' + username
)

github = response.json()

if response.status_code == 200:
  #print(github)

  print("id: ", github["id"])
  print("url: ", github["html_url"])
  print("seguidores: ", github["followers"])
  print("seguindo: ", github["following"])
  print("criado em: ", github["created_at"])

  arquivo = open("github.tsv","a")
  arquivo.write("{}\t{}\n".format(github["id"], github["html_url"]))
  arquivo.close()

else:
  print("Usuário não encontrado!")