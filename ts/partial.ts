type User = {
  id: number;
  name: string;
  email: string;
  isAdmin: boolean;
};

function updateUser(user: User, updates: Partial<User>): User {
  return { ...updates, ...user };
}

let user: User = {
  id: 1,
  name: "asd",
  isAdmin: true,
  email: "asfddas",
};

let change: Partial<User> = {
  id: 1,
  name: "asd",
  isAdmin: true,
};

updateUser(user, change);
