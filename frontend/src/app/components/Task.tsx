import { TaskInterface } from "@/interfaces/TaskInterface";

const Task = (task: TaskInterface) => {
  return (
    <div>
      <h1>{task.title}</h1>
      <p>{task.description}</p>
    </div>
  );
};

export default Task;
