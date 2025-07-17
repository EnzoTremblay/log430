import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 50,
  duration: '30s',
};

export default function () {
  http.get('http://localhost:8080/api/v1/products');
  http.get('http://localhost:8080/api/v1/sales');
  http.get('http://localhost:8080/api/v1/stock');
  http.post('http://localhost:8080/api/v1/clients', JSON.stringify({ nom: 'Alice' }), { headers: { 'Content-Type': 'application/json' } });
  http.post('http://localhost:8080/api/v1/cart', JSON.stringify({ produit_id: 1, quantite: 2 }), { headers: { 'Content-Type': 'application/json' } });
  http.post('http://localhost:8080/api/v1/checkout', JSON.stringify({ cart_id: 1 }), { headers: { 'Content-Type': 'application/json' } });
  sleep(1);
}
