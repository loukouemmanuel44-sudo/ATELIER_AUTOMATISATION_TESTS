# API Choice

- Étudiant : Loukou Emmanuel
- API choisie : JSONPlaceholder
- URL base : https://jsonplaceholder.typicode.com
- Documentation officielle / README : https://jsonplaceholder.typicode.com/guide/
- Auth : None
- Endpoints testés :
  - GET /posts/1
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP : 200 OK
  - Content-Type : application/json; charset=utf-8
  - Champs JSON : userId (int), id (int), title (string), body (string)
- Limites / rate limiting connu : API publique de test sans limite stricte, mais garder un rythme raisonnable (ex. 1 run / 5 minutes)
- Risques (instabilité, downtime, CORS, etc.) : Faible risque de coupure service (fake API stable), aucun problème CORS sur les requêtes serveur
