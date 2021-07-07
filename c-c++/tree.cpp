#include <iostream>
#include <vector>
#include <random>
#include <string>

struct Tree
{
	int value;
	Tree *l_subTree;
	Tree *r_subTree;
};

Tree *create_Tree(int n)
{
	Tree *tree = new Tree();
	*tree = {n, NULL, NULL};
	return tree;
}

void add_Subtree(Tree *tree, int left_value, int right_value)
{
	tree->l_subTree = create_Tree(left_value);
	tree->r_subTree = create_Tree(right_value);
}

void destruct_Tree(Tree *tree)
{
	if (tree->l_subTree != NULL)
	{
		destruct_Tree(tree->l_subTree);
	}
	if (tree->r_subTree != NULL)
	{
		destruct_Tree(tree->r_subTree);
	}
	free(tree);
}

void readTree(Tree *tree, char *identifier, int deepness = 0)
{
	if (deepness > 1)
	{
		for (int i = 0; i < deepness - 1; i++)
		{
			std::cout << "       |";
		}
	}
	if (deepness > 0)
	{
		std::cout << " +---";
	}

	std::cout << identifier << "->" << tree->value << std::endl;

	if (tree->l_subTree != NULL)
	{
		readTree(tree->l_subTree, "L", deepness + 1);
	}
	if (tree->r_subTree != NULL)
	{
		readTree(tree->r_subTree, "R", deepness + 1);
	}
}

Tree *createRandomTree(int maxDepness, int deepness = 0)
{
	if (deepness >= maxDepness)
	{
		return NULL;
	}
	int nodeValue = rand() % 20;
	Tree *tree = create_Tree(nodeValue);
	int numberOfBranches = rand() % 2 + 1;
	int left_or_rigth = rand() % 2;

	if (numberOfBranches == 1)
	{
		if (left_or_rigth)
		{
			tree->r_subTree = createRandomTree(maxDepness, deepness + 1);
			tree->l_subTree = NULL;
		}
		else
		{
			tree->l_subTree = createRandomTree(maxDepness, deepness + 1);
			tree->r_subTree = NULL;
		}
	}
	else
	{

		tree->l_subTree = createRandomTree(maxDepness, deepness + 1);
		tree->r_subTree = createRandomTree(maxDepness, deepness + 1);
	}

	return tree;
}

void traverseTreeInOrder(Tree *tree)
{
	if (tree->l_subTree != NULL)
	{
		traverseTreeInOrder(tree->l_subTree);
	}
	std::cout << tree->value << " ";
	if (tree->r_subTree != NULL)
	{
		traverseTreeInOrder(tree->r_subTree);
	}
}

void traverseTreePreOrder(Tree *tree)
{
	std::cout << tree->value << " ";
	if (tree->l_subTree != NULL)
	{
		traverseTreePreOrder(tree->l_subTree);
	}
	if (tree->r_subTree != NULL)
	{
		traverseTreePreOrder(tree->r_subTree);
	}
}

void traverseTreePostOrder(Tree *tree)
{
	if (tree->l_subTree != NULL)
	{
		traverseTreePostOrder(tree->l_subTree);
	}
	if (tree->r_subTree != NULL)
	{
		traverseTreePostOrder(tree->r_subTree);
	}
	std::cout << tree->value << " ";
}

Tree *createRandomInOrderTree(int maxDepness, int deepness = 0)
{
	if (deepness >= maxDepness)
	{
		return NULL;
	}
	int nodeValue = rand() % 20;
	Tree *tree = create_Tree(nodeValue);
	int numberOfBranches = rand() % 2 + 1;
	int left_or_rigth = rand() % 2;

	if (numberOfBranches == 1)
	{
		if (left_or_rigth)
		{
			tree->r_subTree = createRandomTree(maxDepness, deepness + 1);
			tree->l_subTree = NULL;
		}
		else
		{
			tree->l_subTree = createRandomTree(maxDepness, deepness + 1);
			tree->r_subTree = NULL;
		}
	}
	else
	{

		tree->l_subTree = createRandomTree(maxDepness, deepness + 1);
		tree->r_subTree = createRandomTree(maxDepness, deepness + 1);
	}

	return tree;
}

void BFS(Tree *tree)
{
	static std::vector<Tree *> stack = {};
	if (!stack.empty())
	{
		stack.erase(stack.begin());
	}
	if (tree->l_subTree != NULL)
	{
		stack.push_back(tree->l_subTree);
	}

	if (tree->r_subTree != NULL)
	{
		stack.push_back(tree->r_subTree);
	}

	std::cout << tree->value << " ";
	BFS(stack[0]);
	if (stack.empty())
	{
		return;
	}
}

void DFS(Tree *tree)
{
	std::cout << tree->value << " ";
	if (tree->l_subTree)
	{
		DFS(tree->l_subTree);
	}
	if (tree->r_subTree)
	{
		DFS(tree->r_subTree);
	}
}

std::vector<Tree *> *findNumDFS(Tree *tree, int num, int deepness = 0)
{
	static std::vector<Tree *> stack{};
	if (num == tree->value)
	{
		stack.push_back(tree);
	}

	if (tree->l_subTree)
	{
		findNumDFS(tree->l_subTree, num);
	}
	if (tree->r_subTree)
	{
		findNumDFS(tree->r_subTree, num);
	}
	if (deepness == 0)
	{
		std::vector<Tree *> *response = new std::vector<Tree *>();
		for (auto treePtr : stack)
		{
			(*response).push_back(treePtr);
		}
		stack = {};
	}
}

int main(int argc, char const *argv[])
{
	int treeDeepness;
	std::cin >> treeDeepness;
	Tree *tree = createRandomTree(treeDeepness);
	readTree(tree, "Root");
	DFS(tree);
	std::cout << "\n";
	std::vector<Tree *> *ptrAppearences = findNumDFS(tree, 4);

	return 0;
};