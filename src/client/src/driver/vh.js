// Vue Helper
export const booleanProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: Boolean,
      required: true,
    };
  } else {
    return {
      type: Boolean,
      default: default_,
    };
  }
};

export const numberProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: Number,
      required: true,
    };
  } else {
    return {
      type: Number,
      default: default_,
    };
  }
};

export const stringProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: String,
      required: true,
    };
  } else {
    return {
      type: String,
      default: default_,
    };
  }
};

export const arrayProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: Array,
      required: true,
    };
  } else {
    return {
      type: Array,
      default() {
        return default_;
      },
    };
  }
};

export const objectProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: Object,
      required: true,
    };
  } else {
    return {
      type: Object,
      default() {
        return default_;
      },
    };
  }
};

export const funcProps = (default_) => {
  if (default_ === undefined) {
    return {
      type: Function,
      required: true,
    };
  } else {
    return {
      type: Function,
      default: default_,
    };
  }
};

export const instanceProps = (constructor, default_) => {
  if (default_ === undefined) {
    return {
      required: true,
      validator(any) {
        return any instanceof constructor;
      },
    };
  } else {
    if (default_ !== null && default_ instanceof constructor) {
      throw new Error('The default value of instance props must be instance.');
    }
    return {
      required: false,
      validator(any) {
        return any instanceof constructor;
      },
    };
  }
};

export const multiTypeProps = (typesArray, default_) => {
  if (default_ === undefined) {
    return {
      type: typesArray,
      required: true,
    };
  } else {
    return {
      type: typesArray,
      default: default_,
    };
  }
};

export const unionProps = (type, union, default_) => {
  if (!Array.isArray(union)) {
    throw new Error('union must be an array.');
  }
  const result = {
    type,
    validator(val) {
      return union.includes(val);
    },
  };
  if (default_ === undefined) {
    return {
      ...result,
      required: true,
    };
  } else {
    return {
      ...result,
      default: default_,
    };
  }
};
