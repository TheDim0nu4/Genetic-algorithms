import React from 'react';

const Result = ({ bestItems, profit, weight }) => {
  return (
    <div className="result">
      <center>
        <h2>Profits: {profit}</h2>
        <h2>Weight: {weight}</h2>
        <p>Items that we take:</p>
      </center>
      <ul className="all-items best-items">
        {bestItems.map((el, index) => (
          <li key={index}>
            <pre> Name: {el.name}   Weight: {el.weight}   Value: {el.value} </pre>
          </li>
        ))}
      </ul>
      <br/><br/><br/><br/><br/>
    </div>
  );
};

export default Result;
