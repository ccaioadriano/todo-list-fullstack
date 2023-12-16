import Card from "./components/Task";
import TodoList from "./components/TodoList";
import styles from "./page.module.css";

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
