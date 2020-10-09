#include<stdio.h>

int algarismo (int a) {//Essa função printa um algarismo da Dezena ou da Unidade, considerando a definição diferenciada dos teens
	switch (a) {
//	case 0:
//		printf("zero");
//		break;
//	Zero foi desconsiderado pois não se pronuncia ele.
	case 1:
		printf("um");
		break;
	case 2:
		printf("dois");
		break;
	case 3:
		printf("tres");
		break;
	case 4:
		printf("quatro");
		break;
	case 5:
		printf("cinco");
		break;
	case 6:
		printf("seis");
		break;
	case 7:
		printf("sete");
		break;
	case 8:
		printf("oito");
		break;
	case 9:
		printf("nove");
		break;
	case 10:
		printf("dez");
		break;
	case 11:
		printf("onze");
		break;
	case 12:
		printf("doze");
		break;
	case 13:
		printf("treze");
		break;
	case 14:
		printf("quatorze");//catorze
		break;
	case 15:
		printf("quinze");
		break;
	case 16:
		printf("dezesseis");//dez e seis
		break;
	case 17:
		printf("dezessete");//dez e sete
		break;
	case 18:
		printf("dezoito");//dez oito
		break;
	case 19:
		printf("dezenove");//dez e nove
		break;
	case 20:
		printf("vinte");
		break;
	case 30:
		printf("trinta");
		break;
	case 40:
		printf("quarenta");
		break;
	case 50:
		printf("cinquenta");
		break;
	case 60:
		printf("sessenta");
		break;
	case 70:
		printf("setenta");
		break;
	case 80:
		printf("oitenta");
		break;
	case 90:
		printf("noventa");
		break;
	case 100:
		printf("cem");
		break;//embora seja diferente da ideia geral da função
			//	printar o cem, quando solitário, reduz processamento do Cento
		default: return 0; // caso não dê para printar
	}
	return 1;
}

void extenso (int n) {
	if (n>=1000000) {
		extenso(n/1000000);
		if (n<2000000)
			printf("milhao ");
		else
			printf("milhoes ");
		n = n%1000000;
		if(n==0)
			printf("d"); // de reais
		if(n<=100000 && (n/1000)*(n%1000)==0) //n%1000<=100
			printf("e ");
	}
	if (n>=1000) {
		if(n/1000 > 1) // para não escrever UM MIL
			extenso(n/1000);
		printf("mil ");
		n = n%1000;
		if(n<=100 && n>0)
			printf("e ");
	}
//	if(n==0) return;
	if(n>100)
	{
		switch (n/100)
		{
		case 9:
			printf("novecentos");
			break;
		case 8:
			printf("oitocentos");
			break;
		case 7:
			printf("setecentos");
			break;
		case 6: 
			printf("seiscentos");
			break;
		case 5: 
			printf("quinhentos");
			break;
		case 4:
			printf("quatrocentos");
			break;
		case 3:
			printf("trezentos");
			break;
		case 2:
			printf("duzentos");
			break;
		case 1:	//	caso seja exatamente 100, 100 não é maior que 100, portanto será printado abaixo, e não aqui
			printf("cento"); // devido a isso, este 100 será para quando há algum valor nas unidades e/ou dezenas.
		}
		printf(" "); 
		n %= 100;
		if (n>0) // caso haja algum valor após as centenas, ele deverá ser precedido de E
			printf("e ");
	}
	if (algarismo(n) == 0) // se não foi possível printar, pois é um número com dezena > 1 e unidade > 0
		if (algarismo(n-n%10) == 1) // se foi possível printar a dezena, 
		{
			printf(" e ");
			algarismo(n%10); // printa a unidade. 
		}
	if(n>0)
		printf(" ");
}

void moeda (float v) {
	int reais = (int) v;
	int centavos = (int)100*(v-reais); // possivelmente impreciso
//	printf("%d.%02d = ",reais,centavos);
	if(reais > 0)
	{
		extenso(reais);
		if(reais>1)
			printf("reais");
		else printf("real");
	}
	if (reais*centavos != 0)
		printf(" e ");
	if(centavos > 0)
	{
		extenso(centavos);
		if(centavos==1)
			printf("centavo");
		else printf("centavos");
	}
//	return 100*(v-reais) - centavos;
}

int main () {
	float valor = 0;
/*	for(valor=200;valor<=1111;valor++)
	{
		printf("\nR$%d\t",(int)valor);
		moeda(valor);
	}	*/
	do {
		moeda(valor);		
		printf("\nR$");
		scanf("%f",&valor);
	} while (valor != 0);
	return 0;//(int) valor;
}