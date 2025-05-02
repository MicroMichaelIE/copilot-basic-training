import React from 'react';
import { Cat } from '../types/cat';

interface CatListProps {
    cats: Cat[];
}

export const CatList: React.FC<CatListProps> = ({ cats }) => {
    return (
        <div className="cat-list">
            <h2>Our Cats</h2>
            <div className="cat-grid">
                {cats.map((cat) => (
                    <div key={cat.id} className="cat-card">
                        <h3>{cat.name}</h3>
                        <p>Breed: {cat.breed}</p>
                        <p>Age: {cat.age}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};
