import { use, useState } from "react";
import Task from "./Task";
import { TaskInterface } from "@/interfaces/TaskInterface";

const TodoList = () => {
  const tasks: TaskInterface[] = [
    {
      id: 1,
      title: "Tarefa 1",
      description:
        "loremipsumloremipsumloremipsumloremipsumloremipsumloremipsum",
      completed: true,
    },

    {
      id: 2,
      title: "Tarefa 2",
      description:
        "loremipsumloremipsumloremipsumloremipsumloremipsumloremipsum",
      completed: true,
    },
  ];

  return (
    <>
      <section>
        {tasks.map((task) => {
          return <Task {...task} key={task.id}></Task>;
        })}
      </section>
    </>
  );
};

export default TodoList;
