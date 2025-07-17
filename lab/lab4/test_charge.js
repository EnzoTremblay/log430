import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 50,
  duration: '30s',
};

export default function () {
  http.get('http://localhost:5000/api/v1/stores/1/stock');
  http.get('http://localhost:5000/api/v1/report');
  http.put('http://localhost:5000/api/v1/products/1', JSON.stringify({ nom: 'Outil', prix: 12.0, categorie: 'Bricolage' }), { headers: { 'Content-Type': 'application/json' } });
  sleep(1);
}
