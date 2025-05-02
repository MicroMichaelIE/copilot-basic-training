import { useEffect, useState } from 'react';
import './App.css';
import { CatList } from './components/CatList';
import { CatForm } from './components/CatForm';
import { Cat, CatCreateInput } from './types/cat';
import { CatService } from './services/catService';

function App() {
  const [cats, setCats] = useState<Cat[]>([]);
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadCats();
  }, []);

  const loadCats = async () => {
    try {
      const fetchedCats = await CatService.getAllCats();
      setCats(fetchedCats);
      setError('');
    } catch (err) {
      setError('Failed to load cats');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddCat = async (catData: CatCreateInput) => {
    try {
      const newCat = await CatService.createCat(catData);
      setCats([...cats, newCat]);
      setError('');
    } catch (err) {
      setError('Failed to add new cat');
      console.error(err);
    }
  };

  return (
    <div className="app">
      <h1>Cat Management System</h1>
      {error && <div className="error">{error}</div>}
      {loading ? (
        <div>Loading...</div>
      ) : (
        <>
          <CatForm onSubmit={handleAddCat} />
          <CatList cats={cats} />
        </>
      )}
    </div>
  )
}

export default App
