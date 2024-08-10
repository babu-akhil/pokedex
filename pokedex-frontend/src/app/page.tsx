"use client";

import React, { useEffect, useState } from "react";

interface Pokemon {
  name: string;
  type1: string;
  type2: string;
}

export default function Home() {
  const [pokemon, setData] = useState<Pokemon | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/pokemon/100")
      .then((response) => response.json())
      .then((jsonData) => {
        
          setData(JSON.parse(jsonData)[0])
          console.log(JSON.parse(jsonData)[0])
        })
      .catch((error) => console.log(error));
  }, []);

  return (
    <main>
      {pokemon && (
        <div>
          <pre>{pokemon.name}</pre>
          <pre>{pokemon.type1}</pre>
          </div>
      )}
    </main>
  );
}