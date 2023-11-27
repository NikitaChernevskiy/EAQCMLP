namespace Microsoft.Quantum.Samples {

    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.MachineLearning;
    open Microsoft.Quantum.Math;

    function WithProductKernel(scale : Double, sample : Double[]) : Double[] {
        return sample + [scale * Fold(TimesD, 1.0, sample)];
    }

    function Preprocessed(samples : Double[][]) : Double[][] {
        let scale = 1.0;

        return Mapped(
            WithProductKernel(scale, _),
            samples
        );
    }

    function DefaultSchedule(samples : Double[][]) : SamplingSchedule {
        return SamplingSchedule([
            0..Length(samples) - 1
        ]);
    }

    function ClassifierStructure() : ControlledRotation[] {
        return [
            ControlledRotation((0, new Int[0]), PauliX, 4),
            ControlledRotation((0, new Int[0]), PauliZ, 5),
            ControlledRotation((1, new Int[0]), PauliX, 6),
            ControlledRotation((1, new Int[0]), PauliZ, 7),
            ControlledRotation((0, [1]), PauliX, 0),
            ControlledRotation((1, [0]), PauliX, 1),
            ControlledRotation((1, new Int[0]), PauliZ, 2),
            ControlledRotation((1, new Int[0]), PauliX, 3)
        ];
    }

    function CombineFunction(a: Double, b: Double): Double[] {
        return [a, b];
    }

    function CombineFunction4(a: Double, b: Double, c: Double, d: Double): Double[] {
        return [a, b, c, d];
    }

    operation TrainHalfMoonModel(
        floral : Double[],
        bees : Double[],
        trainingLabels : Int[],
        _1 : Double[],
        _2 : Double[],
        _3 : Double[],
        _4 : Double[],
    ) : (Double[], Double) {
        let trainingVectorsArray = Zipped(floral, bees);
        let trainingVectors = Mapped(CombineFunction, trainingVectorsArray);

        let initialParametersArray = Zipped4(_1, _2, _3, _4);
        let initialParameters = Mapped(CombineFunction4, initialParametersArray);
        let samples = Mapped(LabeledSample,Zipped(Preprocessed(trainingVectors), trainingLabels));

        let (optimizedModel, nMisses) = TrainSequentialClassifier(Mapped(SequentialModel(ClassifierStructure(), _, 0.0), initialParameters),
            samples,
            DefaultTrainingOptions()
                w/ LearningRate <- 0.1
                w/ MinibatchSize <- 15
                w/ Tolerance <- 0.005
                w/ NMeasurements <- 10000
                w/ MaxEpochs <- 16,
            DefaultSchedule(trainingVectors),
            DefaultSchedule(trainingVectors)
        );

        return (optimizedModel::Parameters, optimizedModel::Bias);
    }
}