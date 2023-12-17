import Card from "./components/Task";
import TodoList from "./components/TodoList";

export default function Home() {
  return (
    <>
      <header>
        <h1>Ola Lista de tarefas</h1>
      </header>
      <section>
        <TodoList></TodoList>
      </section>
    </>
  );
}
