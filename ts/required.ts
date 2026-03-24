type DraftUser = {
  name?: string;
  email?: string;
};



let createUser = (user: Required<DraftUser>) => {}




type CompleteUser = Required<DraftUser>; 