import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const PORT = 1245;

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);

  return getAsync(`item.${itemId}`);
}

app.get('/list_products', (request, response) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));

  response.json(products);
});

app.get('/list_products/:itemId', async (request, response) => {
  const { itemId } = request.params;

  const product = getItemById(Number(itemId));

  if (product === undefined) {
    response.status(404).json({
      status: 'Product not found',
    });
    return;
  }

  let currentQuantity = await getCurrentReservedStockById(product.id);

  if (!currentQuantity) {
    currentQuantity = product.stock;
  }

  response.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: Number(currentQuantity),
  });
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const { itemId } = request.params;
  const product = getItemById(Number(itemId));

  if (product === undefined) {
    response.status(404).send({
      status: 'Product not found',
    });
    return;
  }

  let currentQuantity = await getCurrentReservedStockById(product.id);

  if (!currentQuantity) {
    currentQuantity = product.stock;
  }

  currentQuantity = Number(currentQuantity);

  if (!currentQuantity) {
    response.json({ status: 'Not enough stock available', ItemId: product.id });
  } else {
    reserveStockById(product.id, currentQuantity - 1);
    response.json({ status: 'Reservation confirmed', ItemId: product.id });
  }
});

app.listen(PORT, () => {
  console.log('listening on port:', PORT);
});
