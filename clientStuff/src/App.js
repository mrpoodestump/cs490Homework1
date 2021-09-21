import "./App.css";
import StreamData from "./components/StreamData";
import RowCount from "./components/RowCount";
import MostFrequentUser from "./components/MostFrequentUser";

function App() {
  //const { text, pythonError } = runFile;

  return (
    <div>
      <StreamData></StreamData>
      <RowCount></RowCount>
      <MostFrequentUser></MostFrequentUser>
    </div>
  );
}

export default App;
