# Teste da Função `construct_url`

O teste da função `construct_url` avalia se a construção correta da URL de pesquisa do Booking.com com base nos parâmetros fornecidos. A função recebe informações como a data de check-in, data de check-out, destino, número de adultos, número de quartos, número de crianças e a moeda. O objetivo é garantir que a URL gerada esteja formatada corretamente para ser usada em consultas ao site.

## Caso de Teste 1

- **Check-in date:** '2022-01-01'
- **Check-out date:** '2022-01-02'
- **Destination:** 'New York'
- **Adults:** 1
- **Rooms:** 1
- **Children:** 0
- **Currency:** 'USD'

  A URL esperada é: https://www.booking.com/searchresults.en-us.html?checkin=2022-01-01&checkout=2022-01-02&selected_currency=USD&ss=New York&ssne=New York&ssne_untouched=New York&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure


