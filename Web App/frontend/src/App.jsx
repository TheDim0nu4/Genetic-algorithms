import React, { useState } from "react";
import axios from 'axios';
import './css/index.css';
import AddItem from './components/AddItem';
import ItemList from './components/ItemList';
import Result from './components/Result';

const App = () => {
  const [items, setItems] = useState([]);
  const [bestItems, setBestItems] = useState([]);
  const [profit, setProfit] = useState(0);
  const [weight, setWeight] = useState(0);

  const addItem = (newItem) => {
    setItems([...items, newItem]);
  };

  const deleteItem = (index) => {
    let newItems = [...items];
    newItems.splice(index, 1);
    setItems(newItems);
  };

  const getResult = async (maxWeight) => {
    try {
      if (items.length === 0) {
        alert("Add items");
        return;
      }
      if (maxWeight === 0) {
        alert("Enter max weight");
        return;
      }

      let knapsackProblem = { max_weight: maxWeight, items: items };
      let response = await axios.post('http://127.0.0.1:5000/api/main', knapsackProblem, {
        withCredentials: true
      });

      setBestItems(response.data.items);
      setProfit(response.data.fitnes);
      setWeight(response.data.weight);
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  };

  return (
    <div className="App" id="app">
      <h1>Knapsack Calculator</h1>
      <p>Given a set of items, each with a weight and a value. With the help of genetic algorithms, the program determines the items to be included in the collection so that the total weight is less than or equal to a given limit, and the total value is as high as possible.</p>
      <br/><br/>

      <div className="items-container">
        <AddItem addItem={addItem} />
        <ItemList items={items} deleteItem={deleteItem} />
      </div>

      <button className="calc-btn" onClick={() => {
        let maxWeight = Number(document.querySelector('#max-weight').value);
        getResult(maxWeight);
      }}>Calculate</button><br/><br/>

      {bestItems.length > 0 && <Result bestItems={bestItems} profit={profit} weight={weight} />}
    </div>
  );
};

export default App;
