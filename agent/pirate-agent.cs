#r "nuget: Azure.AI.OpenAI"
#r "nuget: Azure.Identity"
#r "nuget: Microsoft.Agents.AI.Hosting"
#r "nuget: Microsoft.Extensions.AI"

    
using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Agents.AI.Hosting;
using Microsoft.Extensions.AI;

var endpoint =
    Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException(
        "AZURE_OPENAI_ENDPOINT is not set.");

var deploymentName =
    Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME")
    ?? throw new InvalidOperationException(
        "AZURE_OPENAI_DEPLOYMENT_NAME is not set.");

// Create Azure OpenAI client
var azureOpenAI = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential());

// Create chat client
IChatClient chatClient = azureOpenAI
    .GetChatClient(deploymentName)
    .AsIChatClient();

// Create the agent
var pirateAgent = new AIAgent(
    chatClient,
    instructions: """
        You are a pirate.
        Speak like a pirate.
        Stay in character.
        Be helpful and concise.
        """);

// Run the agent
var response = await pirateAgent.RunAsync(
    "Ahoy! Tell me about yourself.");

Console.WriteLine(response);
