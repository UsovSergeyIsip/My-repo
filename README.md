[index.html](https://github.com/user-attachments/files/28311004/index.html)

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Игрушки-паровозики</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: 20px auto; padding: 0 10px; }
    input, textarea, button { padding: 8px; margin: 6px 0; width: 100%; box-sizing: border-box; }
    .toy { border: 1px solid #999; padding: 12px; margin: 12px 0; border-radius: 4px; }
    .form-group { margin: 12px 0; }
    label { display: block; font-weight: bold; margin-top: 8px; }
    button { background: #007bff; color: white; border: none; cursor: pointer; }
    button:hover { background: #0056b3; }
    .delete-btn { background: #dc3545; }
    .delete-btn:hover { background: #c82333; }
  </style>
</head>
<body>

<h2>Добавить игрушку-паровозик</h2>
<div class="form-group">
  <label>Номер паровоза (целое число)</label>
  <input type="number" id="locomotive_number" placeholder="123" min="1" />
</div>
<div class="form-group">
  <label>Количество вагонов (целое число)</label>
  <input type="number" id="car_count" placeholder="5" min="0" value="1" />
</div>
<div class="form-group">
  <label>Материал</label>
  <input type="text" id="material" placeholder="Пластик, дерево и т.д." />
</div>
<div class="form-group">
  <label>Описание</label>
  <textarea id="description" placeholder="Описание игрушки..." rows="3"></textarea>
</div>
<button onclick="createToy()">Добавить игрушку</button>

<h2>Список игрушек</h2>
<div id="list"></div>

<script>
async function loadToys() {
  const res = await fetch('/api');
  const toys = await res.json();
  const list = document.getElementById('list');
  if (toys.length === 0) {
    list.innerHTML = '<p>Нет игрушек</p>';
    return;
  }
  list.innerHTML = toys.map(t => `
    <div class="toy">
      <strong>Паровоз №${t.locomotive_number}</strong> (ID: ${t.id})<br>
      Вагонов: ${t.car_count}<br>
      Материал: ${t.material || '—'}<br>
      Описание: ${t.description || '—'}<br>
      <button onclick="editToy(${t.id})">✎ Редактировать</button>
      <button class="delete-btn" onclick="deleteToy(${t.id})">🗑️ Удалить</button>
    </div>
  `).join('');
}

async function createToy() {
  const loco = document.getElementById('locomotive_number').value;
  const cars = document.getElementById('car_count').value;
  const mat = document.getElementById('material').value.trim();
  const desc = document.getElementById('description').value.trim();

  if (!loco || !cars || !mat) {
    alert('Заполните все поля');
    return;
  }

  await fetch('/api/create', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      locomotive_number: parseInt(loco),
      car_count: parseInt(cars),
      material: mat,
      description: desc
    })
  });

  document.getElementById('locomotive_number').value = '';
  document.getElementById('car_count').value = '1';
  document.getElementById('material').value = '';
  document.getElementById('description').value = '';
  loadToys();
}

async function deleteToy(id) {
  if (!confirm('Удалить игрушку? Это нельзя отменить.')) return;
  await fetch(`/api/delete/${id}`, { method: 'POST' });
  loadToys();
}

async function editToy(id) {
  const res = await fetch(`/api/get/${id}`);
  const t = await res.json();
  if (t.error) return alert('Игрушка не найдена');

  const loco = prompt('Номер паровоза', t.locomotive_number);
  if (loco === null || loco === '') return;
  const cars = prompt('Количество вагонов', t.car_count);
  if (cars === null || cars === '') return;
  const mat = prompt('Материал', t.material);
  if (mat === null) return;
  const desc = prompt('Описание', t.description || '');

  await fetch(`/api/update/${id}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      locomotive_number: parseInt(loco),
      car_count: parseInt(cars),
      material: mat,
      description: desc
    })
  });
  loadToys();
}

loadToys();
</script>

</body>
</html>
