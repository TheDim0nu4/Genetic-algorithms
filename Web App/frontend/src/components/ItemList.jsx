import React from 'react';

const ItemList = ({ items, deleteItem }) => {
  return (
    <div className="items">
      <p>Items:</p>
      <ul className="all-items">
        {items.map((el, index) => (
          <li key={index}>
            <pre> Name: {el.name}   Weight: {el.weight}   Value: {el.value} 
              <button title="delete this item" className="del-item" onClick={() => deleteItem(index)}>X</button>
            </pre>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemList;
