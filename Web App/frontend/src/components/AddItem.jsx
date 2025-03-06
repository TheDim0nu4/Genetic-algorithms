import React, { useState } from 'react';

const AddItem = ({ addItem }) => {
  const [name, setName] = useState("");
  const [weight, setWeight] = useState("");
  const [value, setValue] = useState("");

  const handleAddItem = () => {
    if (name === "" || weight === "" || value === "") {
      alert("Incorrectly entered data");
    } else {
      addItem({ name, weight: Number(weight), value: Number(value) });
      setName("");
      setWeight("");
      setValue("");
    }
  };

  return (
    <div className="add-items">
      <p>Enter the maximum backpack weight</p>
      <input type="text" id="max-weight" placeholder="Max weight" autoComplete="off" /><br/>

      <p>Adding an item</p>
      <input type="text" value={name} onChange={e => setName(e.target.value)} placeholder="Name item" autoComplete="off" />
      <input type="text" value={weight} onChange={e => setWeight(e.target.value)} placeholder="Weight item" autoComplete="off" />
      <input type="text" value={value} onChange={e => setValue(e.target.value)} placeholder="Value item" autoComplete="off" />
      <button onClick={handleAddItem} className="add-btn">Add item</button><br/><br/>
    </div>
  );
};

export default AddItem;
