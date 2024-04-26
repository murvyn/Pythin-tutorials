const target = 26;
const nums = [2, 7, 11, 15];

// for (let i = 0; i < nums.length; i++) {
// //   const remain = target - nums[i];
// //   if (nums.includes(remain)) {
// //     if (nums.indexOf(remain) === i) {
// //       continue;
// //     }
// //     console.log(nums.indexOf(remain), i);
// //     break;
// //   }
// }
const add = () => {
  const store = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (store.has(target - nums[i])) {
      return [store.get(target - nums[i]), i];
    }
    store.set(nums[i], i);
  }
};

console.log(add());