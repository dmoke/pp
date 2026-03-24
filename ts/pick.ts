type User1 = {
  id: number;
  name: string;
  email: string;
  password: string;
};

type PublicUser = Pick<User1, "id" | "name" | "email">