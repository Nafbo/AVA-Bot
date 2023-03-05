import React, { useEffect, useState } from "react";

export default function Balanceft() { 
return (
  <div> 
    {fetch("https://ttwjs0n6o1.execute-api.eu-west-1.amazonaws.com/items/1", {mode: 'no-cors'} ).then((response) => {
        console.log(response)
    })}
  </div>
  )
}
