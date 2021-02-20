def is_valid(input):
  matchers = { '(' => ')', '{' => '}', '[' => ']' }
  openers = matchers.keys
  closers = matchers.values
  stack = []

  input.each_char do |c|
    if openers.include?(c)
      stack.push(c)
    elsif closers.include?(c)
      stack.pop == matchers[c]
    end
  end

  stack.size == 0
end